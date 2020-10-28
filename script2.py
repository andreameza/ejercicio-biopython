def summarize_contents(filename):
	listaOs = os.path.split(filename)
	listaExt = os.path.splitext(filename)
	if (listaExt[1] == ".gbk"):
		type_file= "genbank"
	else: 
		type_file= "fasta"
	record = list(SeqIO.parse(filename, type_file))
	#se crea el diccionario
	d = {}
	d['File:'] = listaOs[1]
	d['Path:'] = listaOs[0]
	d['Num_records:'] = len(record)
	#diccionario con listas
	d['Names:'] = []
	d['IDs:'] = []
	d['Descriptions'] = []
	#records
	for seq_rcd in SeqIO.parse(filename,type_file):
		d['Names:'].append(seq_rcd.name)
		d['IDs:'].append(seq_rcd.id)
		d['Descriptions'].append(seq_rcd.description)
	return d

if _name_ == "_main_":
	resultados = summarize_contents(filename)
	print(resultados)
