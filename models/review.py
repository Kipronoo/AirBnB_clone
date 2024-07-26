#!/usr/bin/python3
"""Defines the Review class."""
# models/review.py
from models.base_model import BaseModel

class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
)
