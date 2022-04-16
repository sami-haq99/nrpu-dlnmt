import io
import os
import argparse
import Summzarization_pos as summarization


parser = argparse.ArgumentParser()
parser.add_argument('--lng', type=str, default='en')
parser.add_argument('--startofdoc', default="startofdocumentplaceholder")
parser.add_argument('--ctx-size', default=1, type=int)
args = parser.parse_args()
path = ''
lng = 'en'
print('lng {}'.format(lng))
subsets = ['valid', 'test']
for subset in subsets:
    fn = '{}.bert.{}'.format(subset, lng)
    assert os.path.exists(fn)

print("Using start of doc: %s" % args.startofdoc)
size_str = "" if args.ctx_size == 1 else "{:d}".format(args.ctx_size)
for subset in subsets:
    fn = '{}.bert.{}'.format(subset, lng)
    tgtfn = '{}{}.bert.doc.{}'.format(subset, size_str, lng)
    print("%s  ==>  %s" % (fn, tgtfn))
    prevs = []
    Document = []
    with io.open(fn, 'r', encoding='utf8', newline='\n') as src:
        with io.open(tgtfn, 'w', encoding='utf8', newline='\n') as tgt:
            def write_file(Document, tgt, prevs):
                summary = summarization.generate_summary(Document, 30)
                for sent in Document:
                    newline = '[CLS] {} [SEP] {} [SEP]'.format(' '.join(prevs), sent)
                    if sent in summary:
                        prevs = prevs[max(len(prevs) - args.ctx_size + 1, 0):] + [sent, ]
                    else:
                        prevs = []
                    tgt.write(newline + '\n')

            for line in src:
                line = line.strip()
                if line:
                    if line == args.startofdoc:
                        # End of document is reached

                        if len(Document) != 0:
                            write_file(Document, tgt, prevs)
                            prevs = []
                            Document = []
                    else:
                        Document.append(line)
            #writing last document
            if len(Document) != 0:
                write_file(Document, tgt, prevs)
                prevs = []
                Document = []
    #bpein = path+'/../'+"{}.{}".format(subset, lng)
    #docin =  path+'/'+"{}{}.{}.doc.in".format(subset, size_str, lng)
    #print("Paste: %s + %s  ==>  %s" % (bpein, tgtfn, docin))
    #paste_cmd = "paste -d \"\n\" {} {} > {}".format(bpein, tgtfn, docin)
    #print("cmd: %s" % paste_cmd)
    #os.system(paste_cmd)