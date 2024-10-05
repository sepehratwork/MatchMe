import time

from main import MatchMe
from prompts import test_prompts

match_me = MatchMe()

for subject in test_prompts.keys():
    print(f"{subject}:\n")
    if subject == "Relevant":
        for domain in test_prompts[subject].keys():
            print(f"\n{domain}:")
            prompts = test_prompts[subject][domain]
            for prompt in prompts:
                print(f"Prompt: {prompt}")
                start = time.time()
                result = match_me.extract_domain(prompt)
                end = time.time()
                print(f"Results: {result}    /    Inference Time: {round(end-start,2)}")
    else:
        prompts = test_prompts[subject]
        for prompt in prompts:
            print(f"Prompt: {prompt}")
            start = time.time()
            result = match_me.extract_domain(prompt)
            end = time.time()
            print(f"Results: {result}    /    Inference Time: {round(end-start,2)}")
    print("\n\n" + "-"*100 + "\n\n")