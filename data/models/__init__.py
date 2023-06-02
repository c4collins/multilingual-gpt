from typing import List
from typing import Optional

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text, Enum
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class Base(DeclarativeBase):
    pass
