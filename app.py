#!/usr/bin/env python3

from aws_cdk import core

from hello.hello_stack import MyStack


app = core.App()
MyStack(app, "hello-cdk-1", env={'region': 'eu-west-1'})
MyStack(app, "hello-cdk-2", env={'region': 'eu-west-1'})

app.synth()
