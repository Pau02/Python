#coding : utf8

cajon1=("bebida")
cajon2=("Boligrafo")
cajon3=("Bocadillo")
cajon4=("movil")

mano-extra = cajon1
cajon1     = cajon2
cajon2     = mano-extra
mano-extra = Cajon3
Cajon3     = Cajon4
cajon4     = mano-extra

    print "Cajon1:",cajon1
    print "Cajon2;",cajon2
    print "Cajon1:",cajon3
    print "Cajon2;",cajon4
