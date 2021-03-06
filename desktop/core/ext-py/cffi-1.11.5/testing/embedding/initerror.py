import cffi

ffi = cffi.FFI()

ffi.embedding_api("""
    int add1(int, int);
""")

ffi.embedding_init_code(r"""
    raise KeyError
""")

ffi.set_source("_initerror_cffi", """
""")

fn = ffi.compile(verbose=True)
print('FILENAME: %s' % (fn,))

