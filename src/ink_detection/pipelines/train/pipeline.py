"""
This is a boilerplate pipeline 'train'
generated using Kedro 0.18.7
"""

from kedro.pipeline import Pipeline, node, pipeline


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([node()])
