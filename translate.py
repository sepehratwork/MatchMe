import time
import json
import tqdm
from deep_translator import GoogleTranslator
from langdetect import detect

domains = json.load(open("domain.json", "r"))

for _ in range(10):
    try:
        for domain in domains.keys():
            for intent in domains[domain].keys():
                for i, sample in tqdm.tqdm(enumerate(domains[domain][intent]), desc=f"{domain} - {intent}"):
                    if detect(sample) == "en":
                        translated_text = GoogleTranslator(source='en', target='fa').translate(sample)
                        domains[domain][intent][i] = translated_text
                        json.dump(domains, open("domain_persian.json", "w"), indent=4, ensure_ascii=False)
                        time.sleep(0.1)
    except:
        time.sleep(5)
