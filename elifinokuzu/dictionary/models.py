from django.db import models


LANGUAGE_CHOICES = (
	("tr", "Turkish"),
	("fr", "French"),
	("gr", "German"),
	("pl", "Polish"),
	("kr", "Kurdish"),
	("lt", "Latin"),
	("en", "English"),
	("es", "Spanish"),
)

EDGE_TYPE_CHOICES = (
	("derives_from", "Derives From"),
	("symbol_of", "Symbol Of"),
	("compound_of", "Compound Of"),
)

class Node(models.Model):
	"""
	Node (düğüm)
	The most based entity in the dictionary
	"""
	name = models.CharField(max_length=255)
	language = models.CharField(
		max_length=255,
		choices=LANGUAGE_CHOICES
	)

	def __str__(self):
		return self.name


class Edge(models.Model):
	"""
	Holds the relationships between nodes
	"""
	source = models.ForeignKey(Node, related_name="incoming")
	destination = models.ForeignKey(Node, related_name="outgoing")
	is_directed = models.BooleanField()
	type_of_edge = models.CharField(
		max_length=255,
		choices=EDGE_TYPE_CHOICES
	)