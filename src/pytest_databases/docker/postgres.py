# SPDX-FileCopyrightText: 2023-present Jolt
#
# SPDX-License-Identifier: MIT
from __future__ import annotations

from typing import TYPE_CHECKING

import asyncpg
import pytest

if TYPE_CHECKING:
    from pytest_databases.docker import DockerServiceRegistry


async def postgres_responsive(host: str, port: int, user: str, password: str, database: str) -> bool:
    try:
        conn = await asyncpg.connect(
            host=host,
            port=port,
            user=user,
            database=database,
            password=password,
        )
    except Exception:  # noqa: BLE001
        return False

    try:
        db_open = await conn.fetchrow("SELECT 1")
        return bool(db_open is not None and db_open[0] == 1)
    finally:
        await conn.close()


@pytest.fixture()
def postgres_user() -> str:
    return "postgres"


@pytest.fixture()
def postgres_password() -> str:
    return "super-secret"


@pytest.fixture()
def postgres_database() -> str:
    return "postgres"


@pytest.fixture()
def postgres11_port() -> int:
    return 5422


@pytest.fixture()
def postgres12_port() -> int:
    return 5423


@pytest.fixture()
def postgres13_port() -> int:
    return 5424


@pytest.fixture()
def postgres14_port() -> int:
    return 5425


@pytest.fixture()
def postgres15_port() -> int:
    return 5426


@pytest.fixture()
def postgres16_port() -> int:
    return 5427


@pytest.fixture()
def postgres_default_version() -> str:
    return "postgres16"


@pytest.fixture()
def postgres_port(postgres16_port: int) -> int:
    return postgres16_port


@pytest.fixture()
async def postgres12_service(
    docker_services: DockerServiceRegistry,
    postgres12_port: int,
    postgres_database: str,
    postgres_user: str,
    postgres_password: str,
) -> None:
    await docker_services.start(
        "postgres12",
        timeout=45,
        pause=1,
        check=postgres_responsive,
        port=postgres12_port,
        database=postgres_database,
        user=postgres_user,
        password=postgres_password,
    )


@pytest.fixture()
async def postgres13_service(
    docker_services: DockerServiceRegistry,
    postgres13_port: int,
    postgres_database: str,
    postgres_user: str,
    postgres_password: str,
) -> None:
    await docker_services.start(
        "postgres13",
        timeout=45,
        pause=1,
        check=postgres_responsive,
        port=postgres13_port,
        database=postgres_database,
        user=postgres_user,
        password=postgres_password,
    )


@pytest.fixture()
async def postgres14_service(
    docker_services: DockerServiceRegistry,
    postgres14_port: int,
    postgres_database: str,
    postgres_user: str,
    postgres_password: str,
) -> None:
    await docker_services.start(
        "postgres14",
        timeout=45,
        pause=1,
        check=postgres_responsive,
        port=postgres14_port,
        database=postgres_database,
        user=postgres_user,
        password=postgres_password,
    )


@pytest.fixture()
async def postgres15_service(
    docker_services: DockerServiceRegistry,
    postgres15_port: int,
    postgres_database: str,
    postgres_user: str,
    postgres_password: str,
) -> None:
    await docker_services.start(
        "postgres15",
        timeout=45,
        pause=1,
        check=postgres_responsive,
        port=postgres15_port,
        database=postgres_database,
        user=postgres_user,
        password=postgres_password,
    )


@pytest.fixture()
async def postgres16_service(
    docker_services: DockerServiceRegistry,
    postgres16_port: int,
    postgres_database: str,
    postgres_user: str,
    postgres_password: str,
) -> None:
    await docker_services.start(
        "postgres16",
        timeout=45,
        pause=1,
        check=postgres_responsive,
        port=postgres16_port,
        database=postgres_database,
        user=postgres_user,
        password=postgres_password,
    )


# alias to the latest
@pytest.fixture()
async def postgres_service(
    docker_services: DockerServiceRegistry,
    postgres_default_version: str,
    postgres_port: int,
    postgres_database: str,
    postgres_user: str,
    postgres_password: str,
) -> None:
    await docker_services.start(
        postgres_default_version,
        timeout=45,
        pause=1,
        check=postgres_responsive,
        port=postgres_port,
        database=postgres_database,
        user=postgres_user,
        password=postgres_password,
    )
