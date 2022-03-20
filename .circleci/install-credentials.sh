npx sls config credentials --provider aws --profile user2 --key "$AWS_PROFILE_KEY" --secret "$AWS_PROFILE_SECRET"

( cd step-func ; serverless plugin install --name serverless-step-functions)
