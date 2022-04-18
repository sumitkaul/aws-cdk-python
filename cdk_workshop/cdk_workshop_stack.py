
from constructs import Construct

from aws_cdk import (
    aws_lambda,
    aws_apigateway, 
    aws_kinesis as kinesis,
    core
)

# from .hitcounter import HitCounter

class CdkWorkshopStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        
        my_kinesis= kinesis.Stream(self, "MyFirstStream",
        stream_name="my-awesome-stream"
        )
        
        # my_lambda = aws_lambda.Function(self, 'HelloHandler', 
        #     runtime=aws_lambda.Runtime.PYTHON_3_7,       
        #     code=aws_lambda.Code.from_asset('lambda'), 
        #     handler='hello.handler',
        # )

        # hello_with_counter = HitCounter(self, 'HelloHitCounter',
        #     downstream = my_lambda,
        # )

        # aws_apigateway.LambdaRestApi(self,'Endpoint', 
        #     handler=hello_with_counter._handler,

        # )

        # aws_s3 
        #     path folder 
        # # mykinesis = aws_kinesis.Stream(self, 'MyFirstStream',
        # #     stream_name = "kinesisName"
        # # ) 