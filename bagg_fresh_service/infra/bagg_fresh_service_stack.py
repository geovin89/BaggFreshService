from aws_cdk import (
    aws_lambda as lmb,
    aws_apigateway as apigw,
    CfnOutput,
    Stack,
)
from constructs import Construct
from aws_cdk.aws_apigatewayv2_integrations_alpha import HttpLambdaIntegration
from os import path
from pathlib import Path


class BaggFreshServiceStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        root_dir = Path(path.dirname(__file__)).parent

        handler = lmb.Function(self, 'BaggFreshSellerLambda',
                               runtime=lmb.Runtime.PYTHON_3_8,
                               handler='simple_handler.handler',
                               code=lmb.Code.from_asset(path.join(root_dir, 'src/lambda')))

        bagg_fresh_service_rest_api = apigw.LambdaRestApi(self, 'BaggFreshSellerRestApi',
                                                          handler=handler,
                                                          proxy=False)

        items = bagg_fresh_service_rest_api.root.add_resource('items')
        items.add_method('GET')

        self.url_output = CfnOutput(self, 'BaggFreshSellerRestApiUrl', value=bagg_fresh_service_rest_api.url)
