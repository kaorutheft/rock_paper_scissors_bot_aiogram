from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class LogSettings:
    format: str
    level: str


@dataclass
class Config:
    bot: TgBot
    log: LogSettings


def load_config(path: str) -> Config:
    env = Env()
    env.read_env(path)
    token = env('TOKEN')
    return Config(
        bot=TgBot(token),
        log=LogSettings(
            format=env('LOG_FORMAT'), level=env('LOG_LEVEL')
        )
    )
