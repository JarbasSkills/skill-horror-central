#!/usr/bin/env python3
from setuptools import setup

# skill_id=package_name:SkillClass
PLUGIN_ENTRY_POINT = 'skill-horror-central.jarbasai=skill_horror_central:HorrorCentralSkill'

setup(
    # this is the package name that goes on pip
    name='ovos-skill-horror-central',
    version='0.0.1',
    description='ovos classic horror horror skill plugin',
    url='https://github.com/JarbasSkills/skill-horror-central',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    package_dir={"skill_horror_central": ""},
    package_data={'skill_horror_central': ['locale/*', 'ui/*']},
    packages=['skill_horror_central'],
    include_package_data=True,
    install_requires=["ovos_workshop~=0.0.5a1"],
    keywords='ovos skill plugin',
    entry_points={'ovos.plugin.skill': PLUGIN_ENTRY_POINT}
)
