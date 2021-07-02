import boto3

s3 = boto3.client('s3')
# s3.upload_file('s3_transfer.txt','noria-raspberry-pi','s3_script.txt')
s3.upload_file('Image_IR/image_IR2021-07-02T09.10.06.053475.jpg','noria-raspberry-pi','image_IR.jpg')

