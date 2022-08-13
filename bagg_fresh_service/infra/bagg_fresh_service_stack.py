from aws_cdk import (
    aws_lambda as lmb,
    aws_apigatewayv2_alpha as apigw,
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

        http_api = apigw.HttpApi(self, 'BaggFreshSellerHttpApi')

        http_api.add_routes(
            path="/nearMe",
            methods=[apigw.HttpMethod.GET],
            integration=HttpLambdaIntegration(
                'BaggFreshSellerLambdaIntegration', handler
            )
        )

        self.url_output = CfnOutput(self, 'Url', value=http_api.url)
