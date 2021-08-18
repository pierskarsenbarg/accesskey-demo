"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws

access_key = aws.iam.AccessKey("lbAccessKey",
                               user="testuser-pulumi")

pulumi.export('secret_key', access_key.secret)
