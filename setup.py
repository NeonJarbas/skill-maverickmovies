#!/usr/bin/env python3
from setuptools import setup

# skill_id=package_name:SkillClass
PLUGIN_ENTRY_POINT = 'skill-maverickmovies.jarbasai=skill_maverickmovies:MaverickMoviesSkill'

setup(
    # this is the package name that goes on pip
    name='ovos-skill-maverickmovies',
    version='0.0.1',
    description='ovos Full Free Films skill plugin',
    url='https://github.com/JarbasSkills/skill-maverickmovies',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    package_dir={"skill_maverickmovies": ""},
    package_data={'skill_maverickmovies': ['locale/*', 'ui/*']},
    packages=['skill_maverickmovies'],
    include_package_data=True,
    install_requires=["ovos_workshop~=0.0.5a1"],
    keywords='ovos skill plugin',
    entry_points={'ovos.plugin.skill': PLUGIN_ENTRY_POINT}
)
