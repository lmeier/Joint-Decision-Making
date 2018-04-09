import boto3
MTURK_SANDBOX = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'
mturk = boto3.client('mturk',
   aws_access_key_id = "AKIAIAOJ3KMHSKOI5MUA",
   aws_secret_access_key = "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",
   region_name='us-east-1',
   endpoint_url = MTURK_SANDBOX
)
print("I have $" + mturk.get_account_balance()['AvailableBalance'] + " in my Sandbox account")

question = open(file='questions1.xml',mode='r').read()
new_hit = mturk.create_hit(
    Title = 'What is the category of the image shown?',
    Description = 'Work with AI to categorize images.',
    Keywords = 'categorization, AI, decision-making',
    Reward = '0.0',
    MaxAssignments = 1,
    LifetimeInSeconds = 172800,
    AssignmentDurationInSeconds = 6000,
    AutoApprovalDelayInSeconds = 14400,
    Question = question,
)
print("A new HIT has been created. You can preview it here:")
print("https://workersandbox.mturk.com/mturk/preview?groupId=" + new_hit['HIT']['HITGroupId'])
print("HITID = " + new_hit['HIT']['HITId'] + " (Use to Get Results)")
# Remember to modify the URL above when you're publishing
# HITs to the live marketplace.
# Use: https://worker.mturk.com/mturk/preview?groupId=
