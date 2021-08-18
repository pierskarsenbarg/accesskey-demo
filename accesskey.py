
import pulumi
import pulumi_aws as aws

user = aws.iam.User("test-user")

access_key = aws.iam.AccessKey("access-key",
                               user=user.name)
