from os import path
from constructs import Construct
from aws_cdk import (
    aws_lambda as lmb,
    aws_apigateway as apigw,
    CfnOutput,
    Stack,
)


class BaggFreshServiceStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        root_dir = path.dirname(__file__, '..')

        handler = lmb.Function(self, 'Handler',
                               runtime=lmb.Runtime.PYTHON_3_8,
                               handler='simple_handler.handler',
                               code=lmb.Code.from_asset(path.join(root_dir, 'src/lambda')))

        api_gateway = apigw.LambdaRestApi(self, 'Gateway',
                                          description='Endpoint created for BaggFresh service',
                                          handler=handler.current_version)

        self.url_output = CfnOutput(self, 'Url', value=api_gateway.url)
