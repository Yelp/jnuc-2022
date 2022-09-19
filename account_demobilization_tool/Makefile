VER := 1.0.26
.DEFAULT_GOAL := munkipkg

.PHONY: munkipkg
munkipkg:
	@sed -i.bak -E 's#(.*version.: ).*#\1 "$(VER)"#g' build-info.json
	@rm build-info.json.bak
	@munkipkg .
