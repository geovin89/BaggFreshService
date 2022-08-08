#!/usr/bin/env python3

import aws_cdk as cdk

from bagg_fresh_service.pipeline.bagg_fresh_service_pipeline_stack import BaggFreshServicePipelineStack

app = cdk.App()
BaggFreshServicePipelineStack(app, "BaggFreshServicePipelineStack",
                              env=cdk.Environment(account='141984737041', region='us-west-2')
                              )
app.synth()
