#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel

class State(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
