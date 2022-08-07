#!/usr/bin/env python3

import aws_cdk as cdk

from bagg_fresh_service.bagg_fresh_service_stack import BaggFreshServiceStack


app = cdk.App()
BaggFreshServiceStack(app, "bagg-fresh-service")

app.synth()
