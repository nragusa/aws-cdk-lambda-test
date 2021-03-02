from aws_cdk import core
from aws_cdk import aws_lambda as lambda_
from aws_cdk import aws_lambda_python as lp


class CdkLambdaTestStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Alternative way, equally as crappy
        # myfunc = lambda_.Function(
        #     self, 'MyTestLambda',
        #     code=lambda_.Code.from_asset(path='lambda',
        #                                  bundling={
        #                                      "image": lambda_.Runtime.PYTHON_3_8.bundling_docker_image,
        #                                      "command": ["bash", "-c", "pip install -r requirements.txt -t /asset-output && cp -au . /asset-output"
        #                                                  ]
        #                                  }),
        #     handler='handler',
        #     runtime=lambda_.Runtime.PYTHON_3_8
        # )

        lambda_func = lp.PythonFunction(
            self, 'MyTestLambda',
            entry='lambda'
        )
