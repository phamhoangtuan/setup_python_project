import pytest
from httpx import AsyncClient, Response
from respx import MockRouter

from example_app.app import app


@pytest.mark.asyncio
async def test_get_pokemon(respx_mock: MockRouter) -> None:
    expected_resp: dict = {'pokemon': 'charmandera'}
    number: int = 4

    respx_mock.get(
        url=f'https://pokeapi.co/api/v2/pokemon/{number}'
    ).return_value = Response(status_code=200, json=expected_resp)

    async with AsyncClient(app=app, base_url='http://test') as client:
        url: str = f'/{number}'
        resp: Response = await client.get(url)

        assert resp.json() == expected_resp


@pytest.mark.asyncio
async def test_get_next_pokemon(respx_mock: MockRouter) -> None:
    expected_resp: dict = {'pokemon': 'charmander'}
    number: int = 4

    respx_mock.get(
        url=f'https://pokeapi.co/api/v2/pokemon/{number}'
    ).return_value = Response(status_code=200, json=expected_resp)

    async with AsyncClient(app=app, base_url='http://test') as client:
        url: str = f'/{number}'
        resp: Response = await client.get(url)

        assert resp.json() == expected_resp
