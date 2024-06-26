## Lessons Learned

1) Library adjustments for async operations: If using the openai library and want to do coroutines, make sure to use AsyncOpenAI instead of the base openai modeule. If doing raw requests aiohttp can be used same as always.

2) Limitations of base vision: Specificity is necessary for any kind of ranking system. Left to its own devices, openai gave all cats a ranking of 100. With some adjustments it would give >90% of responses exactly a score of 92. The general context mattered seemingly more than the specific inputs to what should be used in judging.

3) Image URL persistence: openai image urls do not persist. You must provide your own hosting solutions--in this case a s3 bucket.

## .env variables

OPENAI_API_KEY<br />AWS_ACCESS_KEY_ID<br />AWS_SECRET_ACCESS_KEY<br />AWS_REGION<br />BUCKET_NAME

## To run development server

docker-compose up -d --build