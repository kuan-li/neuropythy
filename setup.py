#! /usr/bin/env python

import os
from setuptools import setup

# Deduce the version from the __init__.py file:
version = None
with open(os.path.join(os.path.dirname(__file__), 'neuropythy', '__init__.py'), 'r') as fid:
    for line in (line.strip() for line in fid):
        if line.startswith('__version__'):
            version = line.split('=')[1].strip().strip('\'')
            break
if version is None: raise ValueError('No version found in neuropythy/__init__.py!')

setup(
    name='neuropythy',
    version=version,
    description='Toolbox for flexible cortical mesh analysis and registration',
    keywords='neuroscience mesh cortex registration',
    author='Noah C. Benson',
    author_email='nben@nyu.edu',
    maintainer_email='nben@nyu.edu',
    long_description='''
                     See the README.md file at the github repository for this package:
                     https://github.com/noahbenson/neuropythy
                     ''',
    url='https://github.com/noahbenson/neuropythy',
    download_url='https://github.com/noahbenson/neuropythy',
    license='AGPL',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS'],
    packages=['neuropythy',
              'neuropythy.util',
              'neuropythy.java',
              'neuropythy.io',
              'neuropythy.geometry',
              'neuropythy.optimize',
              'neuropythy.mri',
              'neuropythy.freesurfer',
              'neuropythy.hcp',
              'neuropythy.registration',
              'neuropythy.vision',
              'neuropythy.graphics',
              'neuropythy.datasets',
              'neuropythy.commands',
              'neuropythy.test'],
    include_package_data=True,
    package_data={
        '': ['LICENSE.txt',
             'neuropythy/lib/nben/target/nben-standalone.jar',
             'neuropythy/lib/models/v123.fmm.gz',
             'neuropythy/lib/models/lh.benson17.fmm.gz',
             'neuropythy/lib/models/rh.benson17.fmm.gz',
             'neuropythy/lib/projections/lh.occipital_pole.mp.json',
             'neuropythy/lib/projections/rh.occipital_pole.mp.json',
             'neuropythy/lib/data/fsaverage/surf/lh.benson14_angle.v4_0.mgz',
             'neuropythy/lib/data/fsaverage/surf/lh.benson14_sigma.v4_0.mgz',
             'neuropythy/lib/data/fsaverage/surf/lh.benson14_varea.v4_0.mgz',
             'neuropythy/lib/data/fsaverage/surf/lh.benson14_eccen.v4_0.mgz',
             'neuropythy/lib/data/fsaverage/surf/rh.benson14_retinotopy.v4_0.sphere.reg',
             'neuropythy/lib/data/fsaverage/surf/lh.wang15_mplbl.v1_0.mgz',
             'neuropythy/lib/data/fsaverage/surf/rh.benson14_varea.v4_0.mgz',
             'neuropythy/lib/data/fsaverage/surf/rh.benson14_eccen.v4_0.mgz',
             'neuropythy/lib/data/fsaverage/surf/rh.wang15_mplbl.v1_0.mgz',
             'neuropythy/lib/data/fsaverage/surf/rh.benson14_angle.v4_0.mgz',
             'neuropythy/lib/data/fsaverage/surf/rh.benson14_sigma.v4_0.mgz',
             'neuropythy/lib/data/fsaverage/surf/lh.benson14_retinotopy.v4_0.sphere.reg',
             'neuropythy/lib/data/fsaverage/surf/lh.rosenke18_vcatlas.v1_0.mgz',
             'neuropythy/lib/data/fsaverage/surf/rh.rosenke18_vcatlas.v1_0.mgz',
             'neuropythy/lib/data/fsaverage_sym/surf/lh.benson14_angle.v2_0.mgz',
             'neuropythy/lib/data/fsaverage_sym/surf/lh.benson14_angle.v2_1.mgz',
             'neuropythy/lib/data/fsaverage_sym/surf/lh.benson14_eccen.v3_0.mgz',
             'neuropythy/lib/data/fsaverage_sym/surf/lh.benson14_enorm.v1_0.mgz',
             'neuropythy/lib/data/fsaverage_sym/surf/lh.benson14_angle.v2_5.mgz',
             'neuropythy/lib/data/fsaverage_sym/surf/lh.benson14_varea.v3_0.mgz',
             'neuropythy/lib/data/fsaverage_sym/surf/lh.benson14_eccen.v1_0.mgz',
             'neuropythy/lib/data/fsaverage_sym/surf/lh.benson14_angle.v3_0.mgz',
             'neuropythy/lib/data/fsaverage_sym/surf/lh.benson14_eccen.v2_5.mgz',
             'neuropythy/lib/data/fsaverage_sym/surf/lh.benson14_sigma.v3_0.mgz',
             'neuropythy/lib/data/fsaverage_sym/surf/lh.benson14_varea.v2_5.mgz',
             'neuropythy/lib/data/fsaverage_sym/surf/lh.benson14_angle.v1_0.mgz',
             'neuropythy/lib/data/fsaverage_sym/surf/lh.benson14_varea.v2_0.mgz',
             'neuropythy/lib/data/fsaverage_sym/surf/lh.benson14_varea.v2_1.mgz',
             'neuropythy/lib/data/fsaverage_sym/surf/lh.benson14_eccen.v2_0.mgz',
             'neuropythy/lib/data/fsaverage_sym/surf/lh.benson14_eccen.v2_1.mgz',
             'neuropythy/lib/data/fsaverage_sym/surf/lh.benson14_varea.v1.0.mgz',
             'neuropythy/lib/data/fsaverage_sym/surf/lh.benson14_anorm.v1_0.mgz',
             'neuropythy/lib/data/fsaverage_sym/surf/lh.benson14_retinotopy.v3_0.sphere.reg',
             'neuropythy/lib/data/fs_LR/lh.atlasroi.32k_fs_LR.shape.gii',
             'neuropythy/lib/data/fs_LR/rh.atlasroi.32k_fs_LR.shape.gii',
             'neuropythy/lib/data/fs_LR/lh.atlasroi.59k_fs_LR.shape.gii',
             'neuropythy/lib/data/fs_LR/rh.atlasroi.59k_fs_LR.shape.gii',
             'neuropythy/lib/data/fs_LR/lh.atlasroi.164k_fs_LR.shape.gii',
             'neuropythy/lib/data/fs_LR/rh.atlasroi.164k_fs_LR.shape.gii']},
    install_requires=['numpy>=1.13',
                      'scipy>=1.1',
                      'nibabel>=2.0',
                      'pyrsistent>=0.11',
                      'pint>=0.7',
                      'pimms>=0.3.6',
                      'py4j>=0.10'],
    extras_require={
        'HCP':        ['s3fs>=0.1.5', 'h5py>=2.8.0'],
        'graphics2D': ['matplotlib>=1.5.3'],
        'graphics3D': ['matplotlib>=1.5.3', 'ipyvolume>=0.5.1'],
        'all':        ['s3fs>=0.1.5', 'h5py>=2.8.0', 'matplotlib>=1.5.3', 'ipyvolume>=0.5.1']})
