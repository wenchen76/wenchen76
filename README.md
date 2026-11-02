## Hi, I'm Wenchen Lo 👋

I'm an AI infrastructure engineer focused on LLM inference engine internals and GPU kernel development. I contribute to [SGLang](https://github.com/sgl-project/sglang), [SGLang-Omni](https://github.com/sgl-project/sglang-omni), [vLLM](https://github.com/vllm-project/vllm), and [FlashInfer](https://github.com/flashinfer-ai/flashinfer). Previously, I worked at Apple building ML infrastructure for Siri.


### Merged pull requests 🎉

<!-- merged:start -->
**sgl-project/sglang-omni**

- [[Qwen3-Omni] Keep the thinker's prefill CUDA graph under EAGLE3 drafts](https://github.com/sgl-project/sglang-omni/pull/3247) `#3247`

**sgl-project/sglang**

- [model: adapt mllama4 to VisionAttention](https://github.com/sgl-project/sglang/pull/8512) `#8512`
- [GPTJForCausalLM Support](https://github.com/sgl-project/sglang/pull/7839) `#7839`

**vllm-project/vllm**

- [Remove xformers requirement for Mistral-format Pixtral and Mistral3](https://github.com/vllm-project/vllm/pull/21154) `#21154`
<!-- merged:end -->

### Issues working in progress 🛠️

<!-- working-manual
Add issues you're working on by URL, one per line. Open issues assigned to you are added automatically.
https://github.com/flashinfer-ai/flashinfer/issues/5553
https://github.com/sgl-project/sglang/issues/39299
-->
<!-- working:start -->
**flashinfer-ai/flashinfer**

- [[RL] cuDNN SDPA forward differs across processes on H100 (cuDNN 9.24): document or guard the cudnn attention backend for batch-invariant runs](https://github.com/flashinfer-ai/flashinfer/issues/7982) `#7982`
- [[RL] CUDA-core decode silently ignores disable_split_kv and is batch-variant; backend="auto" should honor or reject the batch-invariance flags](https://github.com/flashinfer-ai/flashinfer/issues/7981) `#7981`
- [SM120 sparse-MLA decode (DSv3.2 / GLM-NSA): chunks_per_block follows the call's total token count, so a request's output depends on the other requests in the step](https://github.com/flashinfer-ai/flashinfer/issues/5553) `#5553`

**sgl-project/sglang**

- [MoE deferred finalize is unreachable for models that supply their own routing (FLASHINFER_TRTLLM_ROUTED excluded)](https://github.com/sgl-project/sglang/issues/39299) `#39299`
<!-- working:end -->

### Pull requests in progress ⏳

<!-- open:start -->
**flashinfer-ai/flashinfer**

- [feat(mla): add batch_invariant to SM120 sparse MLA decode (DSv3.2 / GLM-NSA)](https://github.com/flashinfer-ai/flashinfer/pull/8305) `#8305`

**sgl-project/sglang-omni**

- [[Qwen3-Omni] Support speech output with DFlash and EAGLE3 thinker drafts](https://github.com/sgl-project/sglang-omni/pull/3423) `#3423`
- [[Speculative] Return logprobs for tokens a draft verifies](https://github.com/sgl-project/sglang-omni/pull/3422) `#3422`

**sgl-project/sglang**

- [[Perf] moe: Defer finalize for MXFP8 experts on the routed TRT-LLM runner](https://github.com/sgl-project/sglang/pull/46387) `#46387`
<!-- open:end -->

### Issues reported 📝

<!-- issues:start -->
**sgl-project/sglang**

- [[Bug] MiMo-V2.6 crashes on SM90 (H200) with automatic MoE runner selection: packed MXFP4 experts reach the Triton FP8 runner](https://github.com/sgl-project/sglang/issues/42162) `#42162`
- [[Feature] Add Configurable Per-Modality Input Limits for Multimodal Prompts](https://github.com/sgl-project/sglang/issues/9164) `#9164`

**vllm-project/production-stack**

- [[Doc] Clarify the distinction between Prefix Aware Routing and KV Cache Aware Routing](https://github.com/vllm-project/production-stack/issues/590) `#590`
<!-- issues:end -->

### Other contributions 🗂️

<!-- closed:start -->
**vllm-project/vllm**

- [[Model] Add Support for Grok2](https://github.com/vllm-project/vllm/pull/24286) `PR #24286 · closed`
- [[Feature][Responses API] Browsing Cursor -> Citation](https://github.com/vllm-project/vllm/issues/23220) `Issue #23220 · not planned`
- [Add tuned fused_moe configs for Qwen3-30B-A3B](https://github.com/vllm-project/vllm/pull/23151) `PR #23151 · closed`
- [add lineinfo for all cuda device compilations](https://github.com/vllm-project/vllm/pull/23021) `PR #23021 · closed`
- [[Feature]: Tune Triton Configs for Qwen3-30B-A3-Fp8 and Bf16](https://github.com/vllm-project/vllm/issues/22294) `Issue #22294 · completed`
- [[EPLB] Add EPLB support for dots1](https://github.com/vllm-project/vllm/pull/20870) `PR #20870 · closed`
<!-- closed:end -->
