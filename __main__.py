"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws

access_key = aws.iam.AccessKey("lbAccessKey",
                               user="piers@pulumi.com")

pulumi.export('secret_key', access_key.secret)
