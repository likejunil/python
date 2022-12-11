"""
패키지 배포 순서
1. https://pypi.org 회원 가입
2. 패키지 디렉토리 생성 및 upload 하려는 패키지 환경 파일 준비
    . 패키지 디렉토리 (디렉토리 생성)
        . __init__.py (패키지 인식 파일 생성)
        . {package_name} (파이썬 파일)

    . .gitignore (불필요한 파일들을 upload 하지 않기 위해 설정)
    . LICENCE (https://m.blog.naver.com/occidere/220850682345 참조)
    . MANIFEST.in
    . README.md
    . requirements.txt
    . setup.cfg (옵션)
    . setup.py (필수)
    '''
        << example >>
        setup(
            name='pygifconvt',
            version='1.0.0',
            description='Test package for distribution',
            author='Eunki7',
            author_email='outsider7224@gmail.com',
            url='',
            download_url='',
            install_requires=['pillow'],
            include_package_data=True,
            packages=find_packages(),
            keywords=['GIFCONVERTER', 'gifconverter'],
            python_requires='>=3',
            zip_safe=False,
            classifiers=[
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent"
            ]
        )
    '''

3. pip install setuptools wheel (버그 수정 후에도 여기서 다시 빌드를 한다.)
    - python -m pip install --upgrade setuptools wheel
    - python setup.py sdist bdist_wheel

4. PyPI 배포
    - pip install twine
    - pip -m twine upload dist/*

. git repository 에 source 가 있다면..
pip install git+https://github.com/{path}/{git-file}

"""
