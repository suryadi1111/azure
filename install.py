import os,sys, importlib
def install_module():
    required_modules = ['requests', 'colorama', 'bs4', 'fake_useragent', 'rich', 'tqdm', 'pyfiglet', 'tldextract', 'selenium', 'builtwith', 'bcrypt', 'pytz', 'numpy', 'pystyle', 'paramiko', 'tkinter', 'asyncio', 'aiohttp']
    for module in required_modules:
        try:
            importlib.import_module(module)
        except ImportError:
            try:
                import pip
                pip.main(['install', module])
            except:pass
    print("Done Installing Module")
            
if __name__ == "__main__":
    install_module()