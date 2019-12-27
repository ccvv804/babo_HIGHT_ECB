# babo_HIGHT_ECB
babo HIGHT ECB tool?

Need .so or .dll from https://seed.kisa.or.kr/kisa/Board/18/detailView.do

linux <pre><code>gcc -o KISA_HIGHT_ECB.so -shared -fPIC KISA_HIGHT_ECB.c</code></pre>
windows MinGW <pre><code>gcc -o KISA_HIGHT_ECB.dll -shared -fPIC KISA_HIGHT_ECB.c</code></pre>


encrypt<pre><code>python3 babohightecb.py file e</code></pre>
decrypt<pre><code>python3 babohightecb.py efile d</code></pre>
