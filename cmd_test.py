import os
cmd = ''

dir_para = { \
	'-n ':[10000],\
        #[10000,20000,40000]\
	'-c ':[50,100,200,400],\
	'-t ':[1,2],\
    '--ratio=':['1:10'],\
        #['1:0','1:1','2:1','10:1','1:10','1:2','1:1','0:1'],\
	'--pipeline=':[1],\
        #[1,2,4,8],\
	'-d ':[4096,16384,32768,65536,32,64,128,512,1024]\
	}

i=j=m=n=o=p=0
tmp = ['','','','','','']

#for key,value in dir_para.items():
#	print key,value
for i in range(len(dir_para['-n '])):
    file_name_p = 'redis_cluster/'
    cmd_p = 'memtier_benchmark -p 30001 --show-config '
    tmp[0] = str(dir_para['-n '][i])
    for j in range(len(dir_para['-c '])):
        tmp[1] = str(dir_para['-c '][j])
        for m in range(len(dir_para['-t '])):
            tmp[2] = str(dir_para['-t '][m])
            for n in range(len(dir_para['--ratio='])):
                tmp[3] = str(dir_para['--ratio='][n])
                for o in range( len (dir_para['--pipeline='])):
                    tmp[4] = str (dir_para['--pipeline='][o])
                    for p in range ( len ( dir_para['-d '])):
                        tmp[5] = str( dir_para['-d '][p])
                        file_name = file_name_p +  tmp[0] + '-'\
                                                                + tmp[1] + '-'\
                                                                + tmp[2] + '-'\
                                                                + tmp[3] + '-'\
                                                                + tmp[4] + '-'\
                                                                + tmp[5]
                        cmd = cmd_p + '-n ' + tmp[0] \
                            + ' -c ' + tmp[1]\
                            + ' -t '+tmp[2]\
                            + ' --ratio=' + tmp[3]\
                            + ' --pipeline=' + tmp[4]\
                            + ' --data-size=' + tmp[5]\
                            + ' --out-file=' + file_name\
                            + '\n'
#						print cmd
                        os.system(cmd)
