"""An AWS Python Pulumi program"""
import pulumi
from accesskey import access_key

pulumi.export('secret_key', access_key.secret)
