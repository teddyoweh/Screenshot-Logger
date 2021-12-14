from distutils.core import setup
setup(
  name = 'screenshotLogger',
  packages = ['screenshotLogger'],
  
  license='MIT',
  description = 'Screenshot Logger',
  author = 'Teddy Oweh',
  author_email = 'teddyoweh@gmail.com',
  url = 'https://github.com/teddyoweh/Screenshot-Logger',
  download_url='https://github.com/teddyoweh/Screenshot-Logger/archive/refs/tags/ScreenshotLogger.tar.gz',
  keywords = ['screenshot', 'keylogger', 'logging', 'screenshotlogger'],
  install_requires=[
          'huepy',
          'pyautogui',
      ],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)