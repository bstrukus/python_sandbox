# -*- coding: utf-8 -*-
from . import logic
from .context import helpers

def get_hmm():
    """Get a thought."""
    return 'hmmm...'

def get_hrm():
    """Get a quandry."""
    return '2 + 2'

def hrm():
    """Thinking of a good one..."""
    if logic.get_problem():
        print(get_hrm())

def hmm():
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())