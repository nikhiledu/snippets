#!/usr/bin/env python
import os

def processBlock(registry, repository, tag, zone, target_zone = 'management'):
  print(registry)
  print(repository)
  print(tag)
  print(zone)
  print(target_zone)

registry = os.environ.get('REGISTRY')
repository = os.environ.get('REPOSITORY')
tag = os.environ.get('TAG')
zone = os.getenv('ZONE', 'management')
target_zone = os.environ.get('TARGET_ZONE')

processBlock(registry, repository, tag, zone, target_zone)

