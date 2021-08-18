import pulumi
import pulumi_aws as aws


def create_access_key():
    user = aws.iam.User("test-user")

    return aws.iam.AccessKey("access-key",
                             user=user.name)
