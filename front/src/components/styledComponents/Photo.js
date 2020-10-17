import styled from 'vue-styled-components';

const photoProps = {
	open: Boolean,
	width: String,
	deg: String,
	src: String,
	rate: Number,
};

export const StyledPhotoBlock = styled.section`
	font-size: 32px;
	width: 100%;
	height: 100%;
`;

export const StyledPhoto = styled('div', photoProps)`
	display: inline-block;
	width: ${props => props.width || 20}%;
	height: 0;
	padding-bottom: ${props => props.rate}%;
	transform: rotate(${props => props.deg}deg);
	background-image: url(${props => props.src});
	background-position: center;
	background-size: contain;
	background-repeat: no-repeat;
`;

export const StyledSelectBox = styled('div', photoProps)``;
