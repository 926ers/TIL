llama3가 출시됨

현재 8b, 70b이 공개 되었고 400+b와 다국어 모델은 추후에 공개된다고함

평가 : vocab이 꽤많이 늘었다 12만개? 4배 정도 되었다고 함
한국어 토큰이 들어간거 같다고함 (command r 과 비슷하게 토크나이징 되어서)
한국어 성능은 별루다. -> 중국어 일본어 섞여 나옴
finetune or lora가 필수적일듯

현재 laama3 finetune, lora는 torchtune과 axolotl이 있는데

torchtune은 single gpu에서만 qlora를 지원 multiple gpu에서는 lora만 지원 (현재는)
axolotl은 multiple gpu에서도 qlora를 지원

command r 100b 성능이 꽤나 좋다 