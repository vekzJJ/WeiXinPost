from requests import post

header = {'Authorization': 'token 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',
              "Accept": "application/vnd.github.everest-preview+json"}
r2 = post(f'https://api.github.com/repos/vekzJJ/WeiXinPost/actions/workflows/工作流文件名.yml/dispatches',
              data='{"ref": "main"}',
              headers=header
              )
