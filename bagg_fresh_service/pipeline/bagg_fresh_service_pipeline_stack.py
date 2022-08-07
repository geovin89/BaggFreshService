from constructs import Construct
from aws_cdk import (
    Stack,
)
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep


class BaggFreshServicePipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        CodePipeline(self, 'Pipeline',
                     pipeline_name='BaggFreshServicePipeline',
                     synth=ShellStep("Synth",
                                     input=CodePipelineSource.git_hub("geovin89/BaggFreshService", "main"),
                                     commands=["npm install -g aws-cdk",
                                               "python -m pip install -r requirements.txt",
                                               "cdk synth"]
                                     )
                     )

