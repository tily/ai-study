from transformers import pipeline

text_sim_pipeline = pipeline(
    model="llm-book/bert-base-japanese-v3-jsts",
    function_to_apply="none",
)

text = "川べりでサーフボードを持った人たちがいます"
sim_text = "サーファーたちが川べりに立っています"
result = text_sim_pipeline({"text": text, "text_pair": sim_text})
print(result["score"])

dissim_text = "トイレの壁に黒いタオルがかけられています"
result = text_sim_pipeline({"text": text, "text_pair": dissim_text})
print(result["score"])

from torch.nn.functional import cosine_similarity

sim_enc_pipeline = pipeline(
    model="llm-book/bert-base-japanese-v3-unsup-simcse-jawiki",
    task="feature-extraction",
)

text_emb = sim_enc_pipeline(text, return_tensors=True)[0][0]
sim_emb = sim_enc_pipeline(sim_text, return_tensors=True)[0][0]

sim_pair_score = cosine_similarity(text_emb, sim_emb, dim=0)
print(sim_pair_score.item())

dissim_emb = sim_enc_pipeline(dissim_text, return_tensors=True)[0][0]
dissim_pair_score = cosine_similarity(text_emb, dissim_emb, dim=0)
print(dissim_pair_score.item())
