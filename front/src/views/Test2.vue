<template>
	<v-stage
		ref="stage"
		:config="stageSize"
		@mousedown="handleStageMouseDown"
		@touchstart="handleStageMouseDown"
	>
		<v-layer ref="layer">
			<v-image
				:config="{
					image: image,
					rotation: imageObject.rotation,
					x: imageObject.x,
					y: imageObject.y,
					width: imageObject.width,
					height: imageObject.height,
					scaleX: imageObject.scaleX,
					scaleY: imageObject.scaleY,
					name: 'img',
					draggable: true,
				}"
				@transformend="handleTransformEnd"
			/>
			<v-transformer ref="transformer" />
		</v-layer>
	</v-stage>
</template>

<script>
const width = window.innerWidth;
const height = window.innerHeight;

export default {
	data() {
		return {
			stageSize: {
				width: width,
				height: height,
			},
			image: null,
			imageObject: {
				image: this.image,
				rotation: 0,
				x: 50,
				y: 50,
				width: 100,
				height: 100,
				scaleX: 1,
				scaleY: 1,
				name: 'img',
				draggable: true,
			},
			selectedShapeName: '',
		};
	},
	created() {
		const image = new window.Image();
		image.src = 'https://k3d104.p.ssafy.io/images/emotion/cat/1.png';
		image.onload = () => {
			// set image only when it is loaded
			this.image = image;
		};
	},
	methods: {
		handleTransformEnd(e) {
			// shape is transformed, let us save new attrs back to the node
			// find element in our state
			const imgElem = this.imageObject;
			console.log('rotation', e.target.rotation());
			console.log('x', e.target.x());

			// update the state
			imgElem.x = e.target.x();
			imgElem.y = e.target.y();
			imgElem.rotation = e.target.rotation();
			imgElem.scaleX = e.target.scaleX();
			imgElem.scaleY = e.target.scaleY();
		},
		handleStageMouseDown(e) {
			// clicked on stage - clear selection
			if (e.target === e.target.getStage()) {
				this.selectedShapeName = '';
				this.updateTransformer();
				return;
			}

			// clicked on transformer - do nothing
			const clickedOnTransformer =
				e.target.getParent().className === 'Transformer';
			if (clickedOnTransformer) {
				return;
			}

			// find clicked rect by its name
			const name = e.target.name();

			const imgElem = this.image;
			if (imgElem) {
				this.selectedShapeName = name;
			} else {
				this.selectedShapeName = '';
			}
			this.updateTransformer();
		},
		updateTransformer() {
			// here we need to manually attach or detach Transformer node
			const transformerNode = this.$refs.transformer.getNode();
			const stage = transformerNode.getStage();
			const { selectedShapeName } = this;

			const selectedNode = stage.findOne('.' + selectedShapeName);
			// do nothing if selected node is already attached
			if (selectedNode === transformerNode.node()) {
				return;
			}

			if (selectedNode) {
				// attach to another node
				transformerNode.nodes([selectedNode]);
			} else {
				// remove transformer
				transformerNode.nodes([]);
			}
			transformerNode.getLayer().batchDraw();
		},
	},
};
</script>
