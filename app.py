#!/usr/bin/env python3

from aws_cdk import core

from cdk_lambda_test.cdk_lambda_test_stack import CdkLambdaTestStack


app = core.App()
CdkLambdaTestStack(app, "cdk-lambda-test")

app.synth()
