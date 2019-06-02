# Underwater-Image-Enhancement-via-Style-Transfer (CVPR 2019 WORKSHOP)
This is the official repository for Exemplar Based Underwater Image Enhancement augmented by Wavelet Corrected Transforms.
Paper got accepted at 2019 CVPR Workshop on Automated Analysis of Marine Video for Environmental Monitoring!


In this paper we propose a novel deep learning frame- work to enhance underwater images by augmenting our network with wavelet corrected transformations. Wavelet transforms have recently made way into deep learning frameworks and their ability to reconstruct arbitrary sig- nals accurately makes them favorable for many applica- tions. Underwater images are subjected to unique distor- tions, this is mainly attributed to the fact that red wave- length light gets absorbed dominantly giving a greenish, blue hue. This wavelength dependent selective absorption of light and also scattering by the suspended particles intro- duce non-linear distortions that affect the quality of the im- ages. We propose an encoder-decoder module with wavelet pooling and unpooling as one of the network components to perform progressive whitening and coloring transforms to enhance underwater images via realistic style transfer. We give a sound theoretical proof as to why wavelet transforms are better for signal reconstruction. We demonstrate our proposed framework on popular underwater images dataset and evaluate it using metrics like SSIM, PSNR and UCIQE and show that we achieve state-of-the-art results compared to those mentioned in the literature.


To run the code, Git clone - https://github.com/ClovaAI/WCT2
Follow the instructions provided on that repository to run the code.
For underwater image datasets - http://irvlab.cs.umn.edu/enhancing-underwater-imagery-using-generative-adversarial-networks
TURBID dataset - http://amandaduarte.com.br/turbid/
Check out our results at - https://adarshmj.github.io/page7.html#header2-1d

Providing semantic segmentation maps along with style and content images seems to enhance artistic style transfer, I didnt notice major changes for underwater images. I have also included codes to calculate the SSIM and PSNR values.




To generate semantic segmentation maps you can use the code repository - 
https://github.com/CSAILVision/semantic-segmentation-pytorch

If you are using a non-cuda device and get an error - check out this - https://github.com/CSAILVision/semantic-segmentation-pytorch/issues/117#issuecomment-475057813
