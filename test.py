import time

from main import MatchMe
from prompts import extract_domain_test_prompts, extract_intent_test_prompts, extract_slots_test_prompts


class Test:
    def __init__(self):
        self.match_me = MatchMe()

    def extract_domain(self):
        for subject in extract_domain_test_prompts.keys():
            print(f"\n{subject}:\n")
            if subject == "Relevant":
                for domain in extract_domain_test_prompts[subject].keys():
                    print(f"\n{domain}:")
                    prompts = extract_domain_test_prompts[subject][domain]
                    counter = 0
                    for prompt in prompts:
                        print(f"Prompt: {prompt}")
                        start = time.time()
                        result = self.match_me.extract_domain(prompt)
                        end = time.time()
                        if result == domain:
                            counter += 1
                        print(f"Results: {result}    /    Inference Time: {round(end-start,2)}")
                    accuracy = round((counter / len(prompts)) * 100, 2)
                    print(f"Accuracy of domain {domain}: {accuracy}%")
            else:
                prompts = extract_domain_test_prompts[subject]
                counter = 0
                for prompt in prompts:
                    print(f"Prompt: {prompt}")
                    start = time.time()
                    result = self.match_me.extract_domain(prompt)
                    end = time.time()
                    if result == subject:
                        counter += 1
                    print(f"Results: {result}    /    Inference Time: {round(end-start,2)}")
                accuracy = round((counter / len(prompts)) * 100, 2)
                print(f"Accuracy of domain {subject}: {accuracy}%")
            print("\n\n" + "-"*100 + "\n")

    def extract_intent(self):
        for subject in extract_intent_test_prompts.keys():
            print(f"\n{subject}:\n")
            samples = extract_intent_test_prompts[subject]
            counter = 0
            for prompt, ground_truth in samples:
                start = time.time()
                result = self.match_me.extract_intent(user_prompt=prompt, domain=subject)
                end = time.time()
                print(f"Prompt: {prompt}")
                print(f"Results: {result}    /    Inference Time: {round(end-start,2)}")
                if result == ground_truth:
                    counter += 1
            accuracy = round((counter / len(samples)) * 100, 2)
            print(f"Accuracy of domain {subject}: {accuracy}%")
            print("\n\n" + "-"*100 + "\n")
    
    def extract_slots(self):
        for subject in extract_slots_test_prompts.keys():
            print(f"\n{subject}:\n")
            samples = extract_slots_test_prompts[subject]
            counter = 0
            for ground_truth, prompt in samples:
                start = time.time()
                result = self.match_me.extract_intent(prompt)
                end = time.time()
                print(f"Prompt: {prompt}")
                print(f"Results: {result}    /    Inference Time: {round(end-start,2)}")
                if result == ground_truth:
                    counter += 1
            accuracy = round((counter / len(samples)) * 100, 2)
            print(f"\nAccuracy of domain {subject}: {accuracy}%")
            print("\n\n" + "-"*100 + "\n")


if __name__ == "__main__":
    test = Test()
    test.extract_domain()
    # test.extract_intent()