#!/usr/bin/env python3

import aws_cdk as cdk

from bagg_fresh_service.pipeline.pipeline_stack import PipelineStack

app = cdk.App()
PipelineStack(app, "PipelineStack",
              env=cdk.Environment(account="141984737041", region="us-west-2")
              )
app.synth()
