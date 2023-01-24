import httpx
import uvicorn
from fastapi import FastAPI, HTTPException, Path, status
from httpx import Response

app: FastAPI = FastAPI()


@app.get(path='/{number}', status_code=status.HTTP_200_OK)
def get_pokemon(
    number: int = Path(title='The Pokemon to get (based on number)', ge=1, le=151)
) -> dict:
    """
    Endpoint that returns information about Pokémon.
    Args:
        number: The number of the Pokémon to get
    Returns:
        Awesome information about the Pokémon!
    """
    pokemon_url: str = f'https://pokeapi.co/api/v2/pokemon/{number}'

    try:
        resp: Response = httpx.get(url=pokemon_url)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Could not send a request to {pokemon_url}',
        )

    if resp.status_code == status.HTTP_200_OK:
        return resp.json()
    else:
        raise HTTPException(status_code=resp.status_code, detail=resp.text)


if __name__ == '__main__':
    uvicorn.run(app='app:app', host='127.0.0.1', port=9000, reload=True)
